import { Navigate, Outlet } from "react-router-dom";
import AuthContext from "./AuthProvider";
import { useContext } from "react";

const RequireAuth = () => {
  const { loggedIn, loading } = useContext(AuthContext);

  if (loading) {
    return <></>;
  }

  return loggedIn ? <Outlet /> : <Navigate to="/" />;
};

export default RequireAuth;