import { useState } from "react"

const UserInfoForm = (props) => {
	const [inputs, setInputs] = useState({ phone : ''});

	const handleChange = (event) =>{
		const name = event.target.name;
		const value = event.target.value;
		setInputs(values => ({...values, [name]: value}))
	}

	const handleSubmit = (event) => {
    event.preventDefault();
		props.setTrigger(true);
    // todo: add add user info to db
  }

	return (
		<form className="w-full max-w-lg px-3 mx-auto mt-6">
			<div className="flex flex-wrap -mx-3 mb-6">
				<div className="w-full px-3">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-last-name">
						Phone Number
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-last-name" type="text" placeholder="000-000-0000" name="phone" value={inputs.lastName} onChange={handleChange}/>
				</div>
			</div>
			<div className="mt-8">
				<button className="shadow text-lg bg-green-500 hover:bg-green-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded" type="button" onClick={handleSubmit}>
					Sign Up
				</button>
			</div>
		</form>
)}

export default UserInfoForm