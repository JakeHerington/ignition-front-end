import Head from 'next/head'
import NavBar from '../components/NavBar'
import Dashboard from '../components/Dashboard'

export default function Home() {

  return (
    <>
    <Head>
      <title>Jakes app</title>
      <link rel="icon" href="/favicon.ico" />
    </Head>
    <NavBar />
    <div style={{paddingTop: 54 + 'px'}} />
    <Dashboard />
    </>
  )
}