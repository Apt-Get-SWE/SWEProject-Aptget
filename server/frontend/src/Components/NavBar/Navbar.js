const NavBar = () => (
    <header class="header sticky top-0 bg-white shadow-md flex items-center justify-between px-8 py-02">
        <h1 class="w-3/12">
            <a href="/">
            </a>
        </h1>

        <nav class="nav font-semibold text-lg">
            <ul class="flex items-center">
                <li class="p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer active">
                <a href="/">Market</a>
                </li>
                <li class="p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer">
                <a href="/">Dashboard</a>
                </li>
                <li class="p-4 border-b-2 border-green-500 border-opacity-0 hover:border-opacity-100 hover:text-green-500 duration-200 cursor-pointer">
                <a href="/">Contact</a>
                </li>
            </ul>
        </nav>

        <div class="w-3/12 flex justify-end">
        </div>
    </header>
)

export default NavBar