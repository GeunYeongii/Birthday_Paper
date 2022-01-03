import axios from 'axios'

const service = axios.create({
  baseURL: process.env.VUE_APP_REQUEST_URL,
  timeout: 180000,
  headers: {
    'Content-Type': 'application/json'
  }
})

service.interceptors.response.use(response => {
  return response.data
}, error => {
  console.log(error)
})
  
export default service
  