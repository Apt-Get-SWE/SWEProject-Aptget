import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './Home/Home';
import NotFound from './Pages/NotFound';
import reportWebVitals from './reportWebVitals';
import Register from './Pages/Register/Register';
import CreateItem from './Pages/ItemRelated/CreateItem'
import Dashboard from './Pages/Dashboard';
import Market from './Pages/Market';
import Profile from './Pages/Profile';
import { AuthProvider } from './Auth/AuthProvider';
import RequireAuth from './Auth/RequireAuth';

import {
  Routes,
  Route,
  BrowserRouter,
} from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route element={<RequireAuth />}>
            <Route path="/register" element={<Register />} />
            <Route path="/create" element={<CreateItem />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/market" element={<Market />} />
            <Route path="/profile" element={<Profile />} />
          </Route>
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
