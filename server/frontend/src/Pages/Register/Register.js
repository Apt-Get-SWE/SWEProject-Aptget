import UserInfoForm from "../../Components/Forms/UserInfoForm";
import Notification from "../../Components/Notification/Notification";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
    const [trigger, setTrigger] = useState(false);
    const navigate = useNavigate();

    return (
        <div class="m-10">
            <Notification trigger={trigger} title="Welcome!" description="You are officially an AptGetter" actionPrompt="Go to dashboard" action={
                () => navigate("/dashboard")
            }/>
            <div class="lg:grid lg:grid-cols-5 lg:gap-6">
                <div class="lg:col-span-1"></div>
                <div class="lg:col-span-1 text-center lg:text-left">
                    <div class="px-4 sm:px-0 pt-5">
                        <h3 class="text-xl font-semibold leading-6 text-gray-900">Almost there...</h3>
                        <p class="mt-1 text-lg text-gray-600">Just a few more things we need to know about you.</p>
                    </div>
                </div>
                <div class="mt-5 lg:col-span-2 md:mt-0">
                    <UserInfoForm setTrigger={setTrigger}/>   
                </div>
                <div class="lg:col-span-1"></div>
            </div>
        </div>
    );
}

export default Register