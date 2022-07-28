import './Card.css'

export default function Card({title, onClick}) {return (
    <div onClick={onClick} className="card">
        {title}
    </div>
)}