import React, { useEffect, useState } from 'react';
import { fetchBlockchain } from '../api';

const Blockchain = () => {
  const [blocks, setBlocks] = useState([]);

  useEffect(() => {
    const loadBlockchain = async () => {
      const data = await fetchBlockchain();
      console.log(data); // Verifique a estrutura dos dados
      setBlocks(Array.isArray(data) ? data : []); // Assegura que seja um array
    };
    loadBlockchain();
  }, []);

  return (
    <div>
      <h1>Blockchain</h1>
      <ul>
        {blocks.map(block => (
          <li key={block.index}>
            Índice: {block.index} | Timestamp: {block.timestamp} | Transações: {JSON.stringify(block.transactions)} | Nonce: {block.nonce} | Hash: {block.hash} | Hash Anterior: {block.previous_hash}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Blockchain;
