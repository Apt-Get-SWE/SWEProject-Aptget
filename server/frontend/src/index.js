import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './Home/Home';
import NotFound from './NotFound/NotFound';
import reportWebVitals from './reportWebVitals';
import Register from './Pages/Register/Register';
import CreateItem from './Pages/ItemRelated/CreateItem'
import Dashboard from './Pages/Dashboard';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/register",
    element: <Register />
  },
  {
    path: "/create",
    element: <CreateItem />
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
  },
  {
    path: "*",
    element: <NotFound />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
