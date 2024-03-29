import { useLocation, useNavigate } from 'react-router-dom'

const NavBar = () => {
    const location = useLocation()
    const navigate = useNavigate()

    return (
        <header className="header sticky top-0 bg-white shadow-md flex items-center justify-between px-8 py-2">
            <h1 className="w-3/12">
                <a href="/">
                </a>
            </h1>

            <nav className="nav font-semibold text-lg">
                <ul className="flex items-center">
                    {/* Your existing navigation items */}
                    <li className={location.pathname === '/market'
                        ?
                        "p-4 border-b-2 border-green-500 border-opacity-100 text-green-500 duration-200 cursor-pointer"
                        :
                        "p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer"
                    }
                        onClick={() => {navigate("/market")}}>
                        <span>Market</span>
                    </li>
                    <li className={location.pathname === '/dashboard'
                        ?
                        "p-4 border-b-2 border-green-500 border-opacity-100 text-green-500 duration-200 cursor-pointer"
                        :
                        "p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer"
                    }
                    onClick={() => {navigate("/dashboard")}}>
                        <span>Dashboard</span>
                    </li>
                    <li className={location.pathname === '/profile'
                        ?
                        "p-4 border-b-2 border-green-500 border-opacity-100 text-green-500 duration-200 cursor-pointer"
                        :
                        "p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer"
                    }
                    onClick={() => {navigate("/profile")}}>
                        <span>Profile</span>
                    </li>
                </ul>
            </nav>
            
            <div className="w-3/12 flex justify-end">
                <a href="/api/login/logout">
                    <button
                        className="bg-white border border-green-500 text-green-500 hover:bg-green-500 hover:text-white px-4 py-2 rounded transition duration-200 ease-in-out"
                    >
                        Logout
                    </button>
                </a>
            </div>
        </header>
    )
}

export default NavBar
