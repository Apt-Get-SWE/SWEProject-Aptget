const Notification = (props) => props.trigger ? (
    <div className="fixed z-50 top-1/3 left-1/2 transform -translate-x-1/2 -translate-y-1/2 p-8 bg-white shadow-md hover:shodow-lg rounded-2xl">
        <div className="flex items-center justify-between">
            <div className="flex items-center">
                <svg
                    className="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"
                    viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <div className="flex flex-col ml-3">
                    <div className="font-medium leading-none">{props.title}</div>
                    <p className="text-sm text-gray-600 leading-none mt-1">{props.description}</p>
                </div>
            </div>
            <button className="flex-no-shrink bg-green-500 px-5 ml-4 py-2 text-sm shadow-sm hover:shadow-lg font-medium tracking-wider border-2 border-green-500 text-white rounded-full" onClick={props.action}>{props.actionPrompt}</button>
        </div>
    </div>
) : "";

export default Notification