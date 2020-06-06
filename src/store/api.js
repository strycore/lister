import axios from 'axios'
const BASE_URL = 'http://localhost:5000'

export function getContent (folder, filename) {
  return axios({
    method: 'get',
    url: `${BASE_URL}/${folder}/${filename}`,
    headers: {
      'Content-Type': 'text/plain',
      Accept: 'text/plain'
    }
  })
}

export function updateContent (folder, filename, content) {
  return axios({
    method: 'post',
    url: `${BASE_URL}/${folder}/${filename}`,
    data: content,
    headers: {
      'Content-Type': 'text/plain',
      Accept: 'text/plain'
    }
  })
}
