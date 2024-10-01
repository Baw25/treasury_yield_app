import React from 'react';
import { useParams } from 'react-router-dom';
import OrderForm from './OrderForm';

const EditOrder = () => {
  const { orderId } = useParams();

  return (
    <div>
      <OrderForm orderId={orderId} />
    </div>
  );
};

export default EditOrder;
