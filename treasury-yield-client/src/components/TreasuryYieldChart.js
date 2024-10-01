import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Chart as ChartJS, registerables } from 'chart.js';
import { Chart, Line } from 'react-chartjs-2';
import {
  API_URL,
  TREASURY_YIELDS_LIST_PATH,
} from './constants';
import './TreasuryYieldChart.css';

ChartJS.register(...registerables);

const TreasuryYieldChart = () => {
  const START_TERM = 'one_mo';
  const datasetMapping = {
    one_mo: '1 Month',
    two_mo: '2 Month',
    three_mo: '3 Month',
    four_mo: '4 Month',
    six_mo: '6 Month',
    one_yr: '1 Year',
    two_yr: '2 Year',
    three_yr: '3 Year',
    five_yr: '5 Year',
    seven_yr: '7 Year',
    ten_yr: '10 Year',
    twenty_yr: '20 Year',
    thirty_yr: '30 Year',
  };  

  const [chartData, setChartData] = useState({});
  const [selectedTerm, setSelectedTerm] = useState(START_TERM);
  const [loading, setLoading] = useState(true);
  const [fullData, setFullData] = useState([]);

  const convertDate = (date) => {
    const [_, month, day] = date.split('-');
    return `${month}-${day}`;
  }

  const fetchData = async () => {
    try {
      const response = await axios.get(`${API_URL}${TREASURY_YIELDS_LIST_PATH}`);
      const yieldData = response.data;
      const dates = yieldData.map((item) => convertDate(item.date));

      setFullData(yieldData);
      setChartData({
        labels: dates,
        datasets: [
          {
            label: '1 Month',
            data: yieldData.map((item) => parseFloat(item.one_mo)),
            borderColor: '#e63946',
            fill: false,
          },
        ],
      });

      setLoading(false);
    } catch (error) {
      console.error('Error fetching treasury data:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const updateChart = (termKey) => {
    setChartData({
      labels: fullData.map((item) => convertDate(item.date)),
      datasets: [
        {
          label: datasetMapping[termKey],
          data: fullData.map((item) => parseFloat(item[termKey])),
          borderColor: `#${Math.floor(Math.random() * 16777215).toString(16)}`,
          fill: false,
        },
      ],
    });
  };

  return (
    <div className="chartWrapper">
      <h2>2024 % Yields Over Time Plot</h2>
      <label htmlFor="term-select">Select Term For Plot: </label>
      <select
        id="term-select"
        value={selectedTerm}
        onChange={(e) => {
          setSelectedTerm(e.target.value);
          updateChart(e.target.value);
        }}
      >
        <option value="one_mo">1 Month</option>
        <option value="two_mo">2 Month</option>
        <option value="three_mo">3 Month</option>
        <option value="four_mo">4 Month</option>
        <option value="six_mo">6 Month</option>
        <option value="one_yr">1 Year</option>
        <option value="two_yr">2 Year</option>
        <option value="three_yr">3 Year</option>
        <option value="five_yr">5 Year</option>
        <option value="seven_yr">7 Year</option>
        <option value="ten_yr">10 Year</option>
        <option value="twenty_yr">20 Year</option>
        <option value="thirty_yr">30 Year</option>
      </select>

      {loading ? (
        <p>Loading data...</p>
      ) : (
        <Line
          key={JSON.stringify(chartData)}
          data={chartData}
          options={{
            title: {
              display: true,
              text: `Treasury Yield Curves (${selectedTerm.replace('_', ' ').toUpperCase()})`,
              fontSize: 20,
            },
            scales: {
              xAxes: [
                {
                  type: 'time',
                  time: {
                    unit: 'month',
                    tooltipFormat: 'll',
                    displayFormats: {
                      month: 'MMM YYYY',
                    },
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Date (MM-DD)',
                    fontSize: 16,
                    fontColor: '#333',
                  },
                },
              ],
              yAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: 'Yield Rate (%)',
                    fontSize: 16,
                    fontColor: '#333',
                  },
                },
              ],
            },
          }}
        />
      )}
    </div>
  );
};

export default TreasuryYieldChart;



