import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './OrderList.css';
import {
    API_URL,
    ORDERS_LIST_PATH,
  } from './constants';

const OrdersList = () => {
  const [orders, setOrders] = useState([]);
  const navigate = useNavigate();

  const fetchOrders = async () => {
    try {
      const response = await axios.get(`${API_URL}${ORDERS_LIST_PATH}`);
      setOrders(response.data);
    } catch (error) {
      console.error('Failed to fetch orders:', error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const handleEdit = (orderId) => {
    navigate(`/orders/edit/${orderId}`);
  };

  return (
    <div className="orders-list-container">
      <h2>Historical Orders</h2>
      <table className="orders-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Term</th>
            <th>Amount</th>
            <th>Yield Rate (%)</th>
            <th>Status</th>
            <th>Date of Purchase</th>
            <th>Edit</th>
          </tr>
        </thead>
        <tbody>
          {orders.length > 0 ? (
            orders.map((order) => (
              <tr key={order.id}>
                <td>{order.id}</td>
                <td>{order.term}</td>
                <td>${order.amount.toLocaleString()}</td>
                <td>{order.yield_rate}%</td>
                <td>{order.order_status}</td>
                <td>{new Date(order.date_of_purchase).toLocaleDateString()}</td>
                <td>
                  <button className="edit-button" onClick={() => handleEdit(order.id)}>
                    Edit
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="7">No orders available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default OrdersList;
