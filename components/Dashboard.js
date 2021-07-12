import DailyOutputCard from './DailyOutputCard'
import WeatherCard from './WeatherCard'
import DailyTrendCard from './DailyTrendCard'
import { CardDeck } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

export default function Dashboard() {
    return(
        <CardDeck>
            <DailyOutputCard />
            <WeatherCard /> 
            <DailyTrendCard />
        </CardDeck>
    )
}