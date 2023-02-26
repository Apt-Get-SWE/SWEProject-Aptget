import UserInfoForm from "../../Components/UserInfoForm/UserInfoForm";

const Register = () => (
    <div class="m-10">
        <div class="lg:grid lg:grid-cols-5 lg:gap-6">
            <div class="lg:col-span-1"></div>
            <div class="lg:col-span-1 text-center lg:text-left">
                <div class="px-4 sm:px-0">
                    <h3 class="text-lg font-semibold leading-6 text-gray-900">Almost there...</h3>
                    <p class="mt-1 text-lg text-gray-600">Just a few more things we need to know about you</p>
                </div>
            </div>
            <div class="mt-5 lg:col-span-2 md:mt-0">
                <UserInfoForm />   
            </div>
            <div class="lg:col-span-1"></div>
        </div>
    </div>
)

export default Register