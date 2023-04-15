import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserProfile = () => {
  const [newAddress, setNewAddress] = useState({
    address: '',
    city: '',
    state: '--',
    zipcode: '00000',
  });
  const [createOrAlter, setCreateOrAlter] = useState('create');
  const [userInfo, setUserInfo] = useState({
    fname: '',
    lname: '',
    phone: '',
    email: '',
    pfp: '',
    aid: ''
  });

  const [addressError, setAddressError] = useState('');
  const [cityError, setCityError] = useState('');
  const [stateError, setStateError] = useState('');
  const [zipError, setZipError] = useState('');


  useEffect(() => {
    fetchUserInfo();
    fetchCurrentAddress();
  }, []);

  const fetchUserInfo = async () => {
    try {
      const response = await axios.get('/api/users/get_user_info');
      setUserInfo(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const fetchCurrentAddress = async () => {
    try {
      // Replace the following line with the actual axios call
      const response = await axios.get('/api/users/get_user_address');

      // if response.data is empty dictionary, no need to set state
      if (response.data === {}) {
        setCreateOrAlter('create');
        return;
      } else {
        setNewAddress(response.data);
        setCreateOrAlter('alter');
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleAddAddress = async () => {
    console.log(newAddress)
    const isAddressValid = validateAddress();
    const isCityValid = validateCity();
    const isStateValid = validateState();
    const isZipValid = validateZip();

    if (!isAddressValid || !isCityValid || !isStateValid || !isZipValid) {
      return;
    }
    try {
      console.log(newAddress);
      if (createOrAlter === 'create') {
        const response = await axios.post('/api/users/create_user_address', {
          newAddress,
        });
        console.log(response);
      } else {
        const response = await axios.post('/api/users/alter_user_address', {
          newAddress,
        });
        console.log(response);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    setNewAddress({ ...newAddress, [e.target.name]: e.target.value });
  };

  const validateAddress = () => {
    if (newAddress.address.trim() === '') {
      setAddressError('Address is required.');
      return false;
    } else {
      setAddressError('');
      return true;
    }
  };

  const validateCity = () => {
    if (newAddress.city.trim() === '') {
      setCityError('City is required.');
      return false;
    } else {
      setCityError('');
      return true;
    }
  };

  const validateState = () => {
    if (newAddress.state === '--') {
      setStateError('State is required.');
      return false;
    } else {
      setStateError('');
      return true;
    }
  };

  const validateZip = () => {
    const zipRegex = /^\d{5}$/;
    if (!zipRegex.test(newAddress.zipcode) || newAddress.zipcode === '00000') {
      setZipError('Zip must be valid.');
      return false;
    } else {
      setZipError('');
      return true;
    }
  };


  return (
    <div className="p-6">
      <div className="bg-white rounded-lg shadow-md w-full md:w-3/4 lg:w-1/2 mx-auto p-8">
        <div className="flex flex-col items-center mb-6">
          <img
            className="w-32 h-32 rounded-full mb-4"
            src="https://via.placeholder.com/150"
            alt="User Avatar"
          />
          <h2 className="text-2xl font-semibold">{userInfo.name}</h2>
          <p className="text-gray-500">{userInfo.email}</p>
        </div>

        <div className="w-full">
          <h3 className="text-xl font-semibold mb-4">Address</h3>
          <div className="flex flex-wrap -mx-3 mb-2">
            <div className="w-full px-3">
              <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-address">
                Address
              </label>
              <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-address" type="text" name="address" placeholder="Street / No. / Apt" value={newAddress.address} onChange={handleChange} required />
            <p className="text-red-500 text-xs italic">{addressError}</p>
            </div>
          </div>
          <div className="flex flex-wrap -mx-3">
            <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
              <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-city">
                City
              </label>
              <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-city" type="text" placeholder="City" name="city" value={newAddress.city} onChange={handleChange} required />
            <p className="text-red-500 text-xs italic">{cityError}</p>
            </div>
            <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
              <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-state">
                State
              </label>
              <div className="relative">
                <select className="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-state" name="state" value={newAddress.state} onChange={handleChange}>
                  <option value="--">---</option>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="DC">District Of Columbia</option>
                  <option value="FL">Florida</option>
                  <option value="GA">Georgia</option>
                  <option value="HI">Hawaii</option>
                  <option value="ID">Idaho</option>
                  <option value="IL">Illinois</option>
                  <option value="IN">Indiana</option>
                  <option value="IA">Iowa</option>
                  <option value="KS">Kansas</option>
                  <option value="KY">Kentucky</option>
                  <option value="LA">Louisiana</option>
                  <option value="ME">Maine</option>
                  <option value="MD">Maryland</option>
                  <option value="MA">Massachusetts</option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">New Hampshire</option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">North Carolina</option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">South Carolina</option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">West Virginia</option>
                  <option value="WI">Wisconsin</option>
                  <option value="WY">Wyoming</option>
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                  <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" /></svg>
                </div>
              </div>
            <p className="text-red-500 text-xs italic">{stateError}</p>
            </div>
            <div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
              <label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-zip">
                Zip
              </label>
              <input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-zip" type="text" placeholder="00000" name="zipcode" value={newAddress.zipcode} onChange={handleChange} required />
            <p className="text-red-500 text-xs italic">{zipError}</p>
            </div>
          </div>
          <button className="bg-green-500 hover:bg-green-700 w-full text-white font-bold py-2 px-4 rounded mt-6" type="button" onClick={handleAddAddress}>
            Update Address
          </button>
        </div>
      </div>
    </div>
  );
};

export default UserProfile;
