<template>

  <div class="container">

    <div class="list-group">
      <div class="list-group-item  list-group-item-action" v-for="news in news_list" v-bind:key="news">
        <router-link :to="{name: 'post', params: {url: news.url}}">
          <div class="row">
            <div class="col-4">
              <img class="img-fluid"  :src="news.image">
            </div>
            <div class="col-8">
              <p> {{news.header}} </p>
              <p> {{news.url}} </p>
            </div>
          </div>
          </router-link>
      </div>
    </div>
    <div>
      <ul class="list-group-horizontal">
        <li v-if="previous">
          <button class="btn btn-primary" @click="getNewsList(previous)">Previous</button>
        </li>
        <li  v-if="next">
          <button class="btn btn-primary" @click="getNewsList(next)">Next</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import {APIService} from '../lenta-vue/APIService';
  const apiService = new APIService();

  export default {
    name: 'NewsList',
    data() {
      return {
        news_list: [],
        next: '',
        previous: '',

      };
    },
    methods: {
      getNewsList(url=''){

        this.loading = true;
        apiService.getNewsList(url).then((page) => {
          this.news_list = page.data.results;
          this.next = page.data.next;
          this.previous = page.data.previous;
          this.loading = false;
        });
      },
    },
    mounted() {
      this.getNewsList();
    },
  }
</script>

<style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
