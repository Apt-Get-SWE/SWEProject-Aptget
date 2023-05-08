import axios from "axios";
import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";

const ItemInfoForm = (props) => {
	const [inputs, setInputs] = useState({ itemName: '', desc: '', address: '', city: '', state: '', zipcode: '' });
	const navigate = useNavigate();

	const handleChange = (event) => {
		const name = event.target.name;
		const value = event.target.value;
		setInputs(values => ({ ...values, [name]: value }))
	}

	const toBase64 = (file) => {
		return new Promise((resolve, reject) => {
			const reader = new FileReader();
			reader.readAsDataURL(file);
			reader.onload = () => {
				const base64 = reader.result;
				console.log(base64.substring(0, base64.indexOf(',') + 1));
				const base64Data = base64.substring(base64.indexOf(',') + 1); // Remove prefix
				resolve(base64Data);
			};
			reader.onerror = (error) => reject(error);
		});
	};

	const handleSubmit = async (event) => {
		event.preventDefault();

		if (props.postData) {
			// Update the post
			const payload = {
				pid: props.postData.pid,
				aid: "NOT_USED",
				uid: "NOT_USED",
				title: inputs.itemName,
				descr: inputs.desc,
				image: props.postData.image,
				condition: "new", // dummy
				price: inputs.price,
				sold: "Available",
			};

			axios.put("api/posts/posts", payload, { responseType: 'text' })
				.then((response) => {
					console.log("Post updated successfully", response.data);
					props.setTrigger(true);
				})
				.catch((error) => {
					console.error("Error creating post", error);
					alert(error.response.data);
				});
		} else {
			if (!props.uploaded) {
				alert("Please upload an image");
				return;
			}

			// Convert the image to a base64 string
			const imageBase64 = props.uploaded ? await toBase64(props.uploaded) : "";

			// Create the payload
			const payload = {
				pid: "NOT_USED",
				aid: "NOT_USED",
				uid: "NOT_USED",
				title: inputs.itemName,
				descr: inputs.desc,
				image: imageBase64,
				condition: "new", // dummy
				price: inputs.price,
				sold: "Available",
			};

			// Make the POST request
			axios.post("api/posts/posts", payload, { responseType: 'text' })
				.then((response) => {
					console.log("Post created successfully", response.data);
					props.setTrigger(true);
				})
				.catch((error) => {
					console.error("Error creating post", error);
					alert(error.response.data);
				});
		}
	};

	useEffect(() => {
		// fill in the form if we are editing a post
		console.log(props.postData);
		if (props.postData) {
			setInputs({
				itemName: props.postData.itemName,
				price: props.postData.price,
				desc: ''
			});
		}
	}, []);

	return (
		<form className="w-full max-w-lg px-3 mx-auto mt-6" onSubmit={handleSubmit}>
			<div className="flex flex-wrap -mx-3 mb-6">
				<div className="w-full px-3 mb-4">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-first-name">
						Item Name
					</label>
					<input className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name" type="text" placeholder="Use a descriptive name for your item" name="itemName" value={inputs.itemName} onChange={handleChange} required />
				</div>
				<div className="w-full px-3 mb-2">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-last-name">
						Description
					</label>
					<textarea className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500 h-[20vh] focus:h-[40vh]" id="grid-last-name" type="text" placeholder="Write a description about your item" name="desc" value={inputs.desc} onChange={handleChange} />
				</div>
			</div>

			<div className="flex flex-wrap -mx-3 mb-2">
				<div className="w-full px-3">
					<label className="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" htmlFor="grid-price">
						Price
					</label>
					<input
						className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
						id="grid-price"
						type="number"
						min="0"
						step="0.01"
						name="price"
						placeholder="$0.00"
						value={inputs.price}
						onChange={handleChange}
						required
					/>
				</div>
			</div>

			<div className="mt-8 flex justify-between">
				<button
					className="shadow text-lg bg-red-500 hover:bg-red-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
					type="button"
					onClick={() => navigate("/")}
				>
					Cancel
				</button>
				{
					props.postData ?
						<button
							className="shadow text-lg bg-green-500 hover:bg-green-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
							type="submit"
						>
							Update Listing
						</button>
						:
						<button
							className="shadow text-lg bg-green-500 hover:bg-green-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded"
							type="submit"
						>
							Create Item Listing
						</button>
				}
			</div>
		</form>
	)
}

export default ItemInfoForm