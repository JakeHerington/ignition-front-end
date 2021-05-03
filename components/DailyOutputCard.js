import { Card } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import useSWR from 'swr'
import { format } from 'date-fns'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function DailyOutputCard() {
    
    const API_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/daily-yield"
    const { data, error } = useSWR(API_URL, fetcher)

    if(error) return <div>error</div>
    if(!data) return <div>loading...</div>

    let dailyYield = 0
    data.forEach(value => dailyYield += value)
    let date = format(new Date(), 'PPP')

    return (
        <Card>
            <Card.Header>Total Daily Yield</Card.Header>
            <Card.Body>
                <Card.Subtitle className="mb-2 text-muted">{date}</Card.Subtitle>
                <Card.Text>{dailyYield.toFixed(2)} kW</Card.Text>
            </Card.Body>
        </Card>
    )
}