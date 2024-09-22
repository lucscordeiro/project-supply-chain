import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import ProductDetails from './components/ProductDetails';
import TransactionList from './components/TransactionList';
import Blockchain from './components/Blockchain';
import Navbar from './components/Navbar';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products/:productId" element={<ProductDetails />} />
        <Route path="/transactions" element={<TransactionList />} />
        <Route path="/blockchain" element={<Blockchain />} />
      </Routes>
    </Router>
  );
};

export default App;
