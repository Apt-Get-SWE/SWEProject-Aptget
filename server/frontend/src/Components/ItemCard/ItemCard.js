import './ItemCard.css'

const ItemCard = (props) => (
  <div className="ItemCard">
    <div className="Head">
      <div className="Author">
        <img className="Avatar" src={props.avatar} alt="avatar"/>
        <span className="Username"> {props.username} </span>
      </div>
    </div>
    <img className="Thumbnail" src={props.item_photo} alt="item"/>
    <div className="ContentBody">
      <div className="Details">
        <span className="BuildingName"> {props.building_name} </span>
        <div className="TitleDisc">
          <span className="ItemName"> {props.item_name} </span>
          <span className="Description"> {props.description}</span>
        </div>
      </div>
    </div>
  </div>
)

export default ItemCard