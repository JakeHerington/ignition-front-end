import useSWR from 'swr'

const BASE_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/panel-data?srckey="
const API_URL = "http://localhost:8088/system/webdev/Jakes_Project/api/panel-data?srckey=1BY6WEcLGh8j5v7"

const fetcher = (...args) => fetch(...args).then(res => res.json())

export function getPanelData() {
    //const API_URL = BASE_URL + srckey
    const { data, error } = useSWR(API_URL, fetcher)

    if(error) 
        return "An error occurred"
    else 
        return data
} 