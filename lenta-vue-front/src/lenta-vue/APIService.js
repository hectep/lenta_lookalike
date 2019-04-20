import axios from 'axios';
import constants from '../const'

export class APIService{

    constructor(){

    }

    getNewsList(url){
        if (url==='') {
            url = `${constants.API_URL}/lenta/`;
        }
        return axios.get(url).then(response => response.data);
    }

    getNewsPost(url) {
        const news_post_url = `${constants.API_URL}/post/${url}/`;
        return axios.get(news_post_url).then(response => response.data);
    }
}
