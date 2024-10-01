import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import {
    API_URL,
    ORDERS_CREATE_PATH,
} from './constants';
import './OrderForm.css';

const OrderForm = ({ orderId }) => {
  const [term, setTerm] = useState('');
  const [amount, setAmount] = useState('');
  const [yieldRate, setYieldRate] = useState('');
  const [orderStatus, setOrderStatus] = useState('submitted');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    if (orderId) {
      const fetchOrderData = async () => {
        try {
          const response = await axios.get(`${API_URL}/api/orders/${orderId}/`);
          const order = response.data;

          setTerm(order.term);
          setAmount(order.amount);
          setYieldRate(order.yield_rate);
          setOrderStatus(order.order_status);

        } catch (err) {
          setError('Failed to load orders. Please try again.');
        }
      };

      fetchOrderData();
    }
  }, [orderId]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!term || !amount || !yieldRate) {
      setError('Please complete the order fields.');
      return;
    }

    const payload = {
      term,
      amount: parseFloat(amount),
      yield_rate: parseFloat(yieldRate),
      order_status: orderStatus,
    };

    try {
      if (orderId) {
        // Use update path if order ID is present
        await axios.put(`${API_URL}/api/orders/${orderId}/update`, payload);
        alert('Order updated!');
      } else {
        // Use update path if order ID is not present
        await axios.post(`${API_URL}${ORDERS_CREATE_PATH}`, payload);
        alert('Order created!');
      }

      navigate('/orders');
    } catch (err) {
      setError('Failed to save the order. Please try again.');
    }
  };

  return (
    <div className="order-form-container">
      <h2>{orderId ? `Edit Yield Order ID: ${orderId}` : 'Create New Yield Order'}</h2>
      <form onSubmit={handleSubmit} className="order-form">
        {error && <p className="error">{error}</p>}
        
        <div className="form-group">
          <label htmlFor="term">Term:</label>
          <select id="term" value={term} onChange={(e) => setTerm(e.target.value)} required>
            <option value="">Select Term</option>
            <option value="1M">1 Month</option>
            <option value="3M">3 Month</option>
            <option value="6M">6 Month</option>
            <option value="1Y">1 Year</option>
            <option value="2Y">2 Year</option>
            <option value="5Y">5 Year</option>
            <option value="10Y">10 Year</option>
            <option value="20Y">20 Year</option>
            <option value="30Y">30 Year</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="amount">Amount in USD $</label>
          <input
            type="text"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="yield_rate">Yield Rate %</label>
          <input
            type="text"
            id="yield_rate"
            value={yieldRate}
            onChange={(e) => setYieldRate(e.target.value)}
            placeholder="Enter yield rate"
            required
          />
        </div>

        <button type="submit" className="submit-button">
          {orderId ? 'Update Order' : 'Create Order'}
        </button>
      </form>
    </div>
  );
};

export default OrderForm;