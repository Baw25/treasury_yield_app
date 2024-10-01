import os
import django
import requests
import psycopg2
import datetime
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treasury_app.settings')
django.setup()

from treasury.models import TreasuryYields
from django.db.utils import IntegrityError

# NOTE: Need to change these depending on the Postgres DB configuration 
# CONSTANTS
DB_NAME = 'treasury_db'
DB_USER = 'blakewills' #or default db user / role 
DB_PASSWORD = '' #pull password here via secrets
DB_HOST = 'localhost'
DB_PORT = '5432'
TREASURY_YIELD_DOMAIN = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView"
COLUMN_LENGTH = 14
TREASURY_YEAR = 2024 #Only pull 2024 data 
DATA_SOURCE = 'treasury.gov'
DATA_TYPE = 'Daily Treasury Par Yield Curve Rates'

def get_treasury_yield_domain(type_input: str, tdr_date_value: str) -> list:
    return f'{TREASURY_YIELD_DOMAIN}?type={type_input}&field_tdr_date_value={tdr_date_value}'

def get_treasury_yield_data() -> None:
    url = get_treasury_yield_domain('daily_treasury_yield_curve', str(TREASURY_YEAR))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    treasury_data = []

    for row in rows[1:]:
        columns = row.find_all('td')
        date_str = columns[0].text.strip()
        date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()

        row_data = {}
        yields = []
        # Order -> Date, 1 Mo, 2 Mo, 3 Mo, 4 Mo, 6 Mo, 1 Yr, 2 Yr, 3 Yr, 5 Yr, 7 Yr, 10 Yr, 20 Yr, 30 Yr
        for col in columns[1:]:
            if col.text.strip() != 'N/A': 
                yields.append(float(col.text.strip()))

        row_data["date"] = date
        row_data["yields"] = yields
        treasury_data.append(row_data)            

    return treasury_data

def save_to_database(yield_data) -> None:

    treasury_records = []
    for data in yield_data:
        date = data["date"]
        yields = data["yields"]

        treasury_record = TreasuryYields(
            date=date,
            one_mo=yields[0] if len(yields) > 0 else None,
            two_mo=yields[1] if len(yields) > 1 else None,
            three_mo=yields[2] if len(yields) > 2 else None,
            four_mo=yields[3] if len(yields) > 3 else None,
            six_mo=yields[4] if len(yields) > 4 else None,
            one_yr=yields[5] if len(yields) > 5 else None,
            two_yr=yields[6] if len(yields) > 6 else None,
            three_yr=yields[7] if len(yields) > 7 else None,
            five_yr=yields[8] if len(yields) > 8 else None,
            seven_yr=yields[9] if len(yields) > 9 else None,
            ten_yr=yields[10] if len(yields) > 10 else None,
            twenty_yr=yields[11] if len(yields) > 11 else None,
            thirty_yr=yields[12] if len(yields) > 12 else None,
            source=DATA_SOURCE,
            interest_rate_data_type=DATA_TYPE,
            time_period=str(TREASURY_YEAR)
        )

        treasury_records.append(treasury_record)

    try:
        TreasuryYields.objects.bulk_create(treasury_records)
        print(f"Saved {len(treasury_records)} records")
    except IntegrityError as e:
        print(f"Error saving records: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")  

if __name__ == "__main__":
    yield_data = get_treasury_yield_data()
    save_to_database(yield_data)
