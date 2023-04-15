import bg from './BgIllustration.svg'
import { useContext, useEffect } from 'react';
import AuthContext from '../Auth/AuthProvider';
import { useNavigate } from 'react-router-dom';

function Home() {
  const { loggedIn } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (loggedIn) {
      navigate('/dashboard');
    }
  }, [loggedIn, navigate]);

  return (
    <div className="min-h-screen bg-gradient-to-b from-green-300 to-green-700 flex flex-col justify-center items-center">
      <div className="flex flex-wrap items-center justify-center">
        <div className="w-full lg:w-1/4 bg-white rounded-lg shadow p-8 mr-8 hidden lg:block">
          <h2 className="text-4xl font-semibold text-green-700 mb-6">
            AptGet<span className='text-black'>.nyc</span>
          </h2>
          <p className="text-lg text-green-700 mb-4">
            AptGet is an innovative platform that connects apartment dwellers, enabling them to trade stuff easily and efficiently.
          </p>
          <p className="text-lg text-green-700">
            Join our community and enjoy a hassle-free experience of trading goods and services between apartments!
          </p>
          <a href='/api/login/login'>
            <button type="button" className="text-white bg-[#4285F4] hover:bg-[#4285F4]/90 focus:ring-4 focus:outline-none focus:ring-[#4285F4]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#4285F4]/55 ml-0 mb-0 mt-5">
              <svg className="w-4 h-4 mr-2 -ml-1" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="google" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 488 512"><path fill="currentColor" d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"></path></svg>
              Sign in with Google
            </button>
          </a>
        </div>
        <div className="lg:w-2/3 h-full relative">
          <img
            src={bg}
            alt="Hero"
            className="rounded-lg object-cover h-[99vh] w-full"
          />
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="w-full ml-20">
              <p className="text-3xl text-white mb-2 z-10">
                See what people are trading around your location...
              </p>
              <input
                type="search"
                placeholder="What's your address?"
                className="border border-green-300 p-2 w-2/3 focus:ring-2 focus:ring-green-500 focus:outline-none z-10 rounded-full"
              />
              <button className="bg-white hover:bg-green-200 ring-green-500 focus:ring-green-300 font-medium rounded-full text-sm px-5 py-2.5 text-center z-10 ml-2"> Search
              </button>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
