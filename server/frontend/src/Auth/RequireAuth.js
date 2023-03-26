import { Navigate, Outlet } from "react-router-dom";
import AuthContext from "./AuthProvider";
import axios from "axios";
import { useContext, useEffect, useState } from "react";

const RequireAuth = () => {
  const { loggedIn, loading } = useContext(AuthContext);

  if (loading) {
    return <></>;
  }

  return loggedIn ? <Outlet /> : <Navigate to="/" />;
};

export default RequireAuth;