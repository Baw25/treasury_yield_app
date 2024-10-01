import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TreasuryYieldChart from './components/TreasuryYieldChart';
import NewOrder from './components/NewOrder';
import Navbar from './components/Navbar';
import OrdersList from './components/OrderList';
import EditOrder from './components/EditOrder';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<TreasuryYieldChart />} />
        <Route path="/new-order" element={<NewOrder />} />
        <Route path="/orders" element={<OrdersList />} />
        <Route path="/orders/edit/:orderId" element={<EditOrder />} />       
      </Routes>
    </Router>
  );
};

export default App;
