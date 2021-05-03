import 'bootstrap/dist/css/bootstrap.min.css'
import { format } from 'date-fns'
import { Card } from 'react-bootstrap'
import DailyTrendChart from './DailyTrendChart'

export default function DailyTrendCard() {

    let date = format(new Date(), 'PPP')
    console.log("Before Trend Card Render")
    return (
        <Card>
            <Card.Header>Yesterday Trend</Card.Header>
            <Card.Body>
                <Card.Subtitle className="mb-2 text-muted">{date}</Card.Subtitle>
                <DailyTrendChart />
            </Card.Body>
        </Card>
    )
}