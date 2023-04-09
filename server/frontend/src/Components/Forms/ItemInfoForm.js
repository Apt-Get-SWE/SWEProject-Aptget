import { useState } from "react"

const ItemInfoForm = (props) => {
	const [inputs, setInputs] = useState({ itemName: '', desc: '', address: '', city: '', state: '', zipcode: ''});

	const handleChange = (event) =>{
		const name = event.target.name;
		const value = event.target.value;
		setInputs(values => ({...values, [name]: value}))
	}

	const handleSubmit = (event) => {
		event.preventDefault();
		props.setTrigger(true);
    // todo: add Item to db
  }

	return (
		<form className="w-full max-w-lg px-3 mx-auto mt-6" onSubmit={handleSubmit}>
			<div className="flex flex-wrap -mx-3 mb-6">
				<div className="w-full px-3 mb-4">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-first-name">
						Item Name
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="text" placeholder="Use a descriptive name for your item" name="itemName" value={inputs.itemName} onChange={handleChange} required/>
				</div>
				<div className="w-full px-3 mb-2">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-last-name">
						Description
					</label>
					<textarea className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500 h-[20vh] focus:h-[40vh]" id="grid-last-name" type="text" placeholder="Write a description about your item" name="desc" value={inputs.desc} onChange={handleChange}/>
				</div>
			</div>

			<div className="flex flex-wrap -mx-3 mb-2">
				<div className="w-full px-3">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-address">
						Address
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-address" type="text" name="address" placeholder="Street / No. / Apt" value={inputs.address} onChange={handleChange} required/>
				</div>
			</div>

			<div className="flex flex-wrap -mx-3">
				<div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-city">
						City
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-city" type="text" placeholder="City" name="city" value={inputs.city} onChange={handleChange} required/>
				</div>
				<div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-state">
						State
					</label>
					<div className="relative">
						<select className="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-state" name="state" value={inputs.state} onChange={handleChange}>
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
				</div>

				<div className="w-full md:w-1/3 px-3 mb-6 md:mb-0">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-zip">
						Zip
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-zip" type="text" placeholder="00000" name="zipcode" value={inputs.zipcode} onChange={handleChange} required/>
				</div>
				
			</div>
			<div className="mt-8 flex justify-between">
			<button
				className="shadow text-lg bg-red-500 hover:bg-red-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
				type="button"
				onClick={() => props.setTrigger(false)}
			>
				Cancel
			</button>
			<button
				className="shadow text-lg bg-green-500 hover:bg-green-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
				type="submit"
			>
				Create Item Listing
			</button>
			</div>
		</form>
)}

export default ItemInfoForm