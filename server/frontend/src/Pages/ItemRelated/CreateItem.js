import ItemInfoForm from "../../Components/Forms/ItemInfoForm";
import Notification from "../../Components/Notification/Notification";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const CreateItem = () => {
    const [trigger, setTrigger] = useState(false);
    const [uploaded, setUploaded] = useState(null);
    const navigate = useNavigate();

    const handleUpload = (event) => {
        setUploaded(event.target.files[0])
    }

    const [hover, setHover] = useState(false);

    return (
        <div className="m-10">
            <Notification trigger={trigger} title="You're all set" description="Successfully Created Item Listing" actionPrompt="Go to dashboard" action={
                () => navigate("/")
                // TODO: axios post item
            } />
            {
                trigger ? 
                <div className="fixed top-0 left-0 w-full h-full bg-black opacity-50 z-10 pointer-events-auto"></div>
                :
                null
            }
            <div className="lg:grid lg:grid-cols-5 lg:gap-6">
                <div className="lg:col-span-1"></div>
                <div className="lg:col-span-1 text-center lg:text-left">
                    <div className="px-4 sm:px-0 pt-5">
                        <h3 className="text-xl font-semibold leading-6 text-gray-900">Almost there...</h3>
                        <p className="mt-1 text-lg text-gray-600">Please fill in the details of your listing</p>
                    </div>
                    <div className="border border-green-500 p-3 pt-0 mt-5 text-center rounded-lg">
                    <p className="mt-1 text-lg text-gray-600">Item Photo</p>
                    {
                        uploaded ?
                            <div className="relative group" onMouseEnter={() => {setHover(true);}} onMouseLeave={() => {setHover(false);}}>
                                <img src={URL.createObjectURL(uploaded)} alt="Item Uploaded" className="aspect-square w-full object-cover rounded-lg" />
                                {hover &&
                                    <div className="absolute inset-0 bg-gray-800 opacity-0 group-hover:opacity-75 transition-opacity">
                                        <button className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-red-600 text-white px-4 py-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity" onClick={() => setUploaded(null)}>Delete</button>
                                    </div>
                                }
                            </div>
                            :
                            <div className="flex items-center justify-center w-full">
                                <label for="dropzone-file" className="flex flex-col items-center justify-center w-full aspect-square border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                        <svg aria-hidden="true" className="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                                        <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span></p>
                                        <p className="text-xs text-gray-500 dark:text-gray-400">PNG or JPG</p>
                                    </div>
                                    <input id="dropzone-file" accept=".jpeg, .jpg, .png" type="file" className="hidden" onChange={handleUpload} />
                                </label>
                            </div>
                    }
                    </div>
                </div>
                <div className="mt-5 lg:col-span-2 md:mt-0">
                    <ItemInfoForm setTrigger={setTrigger} uploaded={uploaded}/>
                </div>
                <div className="lg:col-span-1"></div>
            </div>
        </div>
    );
}

export default CreateItem