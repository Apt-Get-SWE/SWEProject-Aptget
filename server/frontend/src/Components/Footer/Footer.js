const Footer = () => (
    <div>
        <footer aria-label="Site Footer" className="bg-white text-center">
            <div className="mx-auto max-w-screen-xl px-4 py-12 sm:px-6 lg:px-8">
                <div className="mx-auto max-w-3xl space-y-6">

                    <nav
                        aria-label="Footer Nav"
                        className="rounded-3xl border-4 border-gray-900 p-6"
                    >
                        <ul className="flex flex-wrap justify-center gap-6 text-sm font-bold">
                            <li>
                                <a
                                    className="text-gray-900 transition hover:text-gray-900/75"
                                    href="/"
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    Contact
                                </a>
                            </li>

                            <li>
                                <a
                                    className="text-gray-900 transition hover:text-gray-900/75"
                                    href="/"
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    Help Center
                                </a>
                            </li>

                            <li>
                                <a
                                    className="text-gray-900 transition hover:text-gray-900/75"
                                    href="/"
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    Change Log
                                </a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </footer>
    </div>
)

export default Footer