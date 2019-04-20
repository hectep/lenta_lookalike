import NewsList from './components/NewsList'
import NewsPost from './components/NewsPost'


const routes = [
    { path: '/', component: NewsList },
    { path: '/post/:url', component: NewsPost, name: 'post' },
];
export default routes;