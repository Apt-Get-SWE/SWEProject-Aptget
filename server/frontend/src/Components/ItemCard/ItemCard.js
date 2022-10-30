import './ItemCard.css'

const ItemCard = (props) => (
  <div className="ItemCard">
    <div className="Head">
      <div className="Author">
        <img className="Avatar" src={props.info.avatar} alt="avatar"/>
        <span className="Username"> {props.info.username} </span>
      </div>
    </div>
    <img className="Thumbnail" src={props.info.item_photo} alt="item"/>
    <div className="ContentBody">
      <div className="Details">
        <span className="BuildingName"> {props.info.building_name} </span>
        <div className="TitleDisc">
          <span className="ItemName"> {props.info.item_name} </span>
          <span className="Description"> {props.info.description}</span>
        </div>
      </div>
    </div>
  </div>
)

export default ItemCard