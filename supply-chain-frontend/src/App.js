import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddProduct from './components/AddProduct';
import RegisterStage from './components/RegisterStage';
import TrackProduct from './components/TrackProduct';
import ReportsAndAlerts from './components/ReportsAndAlerts';
import Home from './components/Home';

const App = () => {
    return (
        <Router>
            <div className="App">
                <h1>Supply Chain Management</h1>
                <Routes>
                    <Route path="/add-product" element={<AddProduct />} />
                    <Route path="/register-stage" element={<RegisterStage />} />
                    <Route path="/track-product" element={<TrackProduct />} />
                    <Route path="/reports-alerts" element={<ReportsAndAlerts />} />
                    <Route path="/" element={<Home/>} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
