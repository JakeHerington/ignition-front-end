import { Card } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import useSWR from 'swr'
import { format } from 'date-fns'
import Thermo from'react-thermo'

const fetcher = (...args) => fetch(...args).then(res => res.json())

export default function TemperatureCard() {
    
    const API_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/current-temp"
    const { data, error } = useSWR(API_URL, fetcher)

    if(error) return <div>error</div>
    if(!data) return <div>loading...</div>

    let date = format(new Date(), 'PPP')
    
    return (
        <Card>
            <Card.Header>Current Temperature</Card.Header>
            <Card.Body>
                <Card.Subtitle className="mb-2 text-muted">{date}</Card.Subtitle>
                <Thermo min={-10} max={50} temperature={data.value} zones={[10,30]} />
                <Card.Text>{data.value} °C</Card.Text>
            </Card.Body>
        </Card>
    )
}

