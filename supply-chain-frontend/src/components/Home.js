import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div>
            <h2>Welcome to the Supply Chain Management System</h2>
            <nav>
                <ul>
                    <li>
                        <Link to="/add-product">Add Product</Link>
                    </li>
                    <li>
                        <Link to="/register-stage">Register Stage</Link>
                    </li>
                    <li>
                        <Link to="/track-product">Track Product</Link>
                    </li>
                    <li>
                        <Link to="/reports-alerts">Reports and Alerts</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default Home;
