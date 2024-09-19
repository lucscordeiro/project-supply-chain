// src/components/TransactionList.js
import React, { useEffect, useState } from 'react';
import { fetchTransactions } from '../api';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const loadTransactions = async () => {
      const data = await fetchTransactions();
      console.log(data); // Verifique a estrutura dos dados
      setTransactions(Array.isArray(data) ? data : []); // Assegura que seja um array
    };
    loadTransactions();
  }, []);

  return (
    <div>
      <h1>Lista de Transações</h1>
      <ul>
        {transactions.map(transaction => (
          <li key={transaction.id}>
            Transação ID: {transaction.id} | Produto: {transaction.product_id} | De: {transaction.from_entity} | Para: {transaction.to_entity} | Data: {transaction.timestamp}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionList;
