<template>
    <div class="container">
        <div>
            <div class="row">
                <div class="col-4">
                    <img class="img-fluid"  :src="news_data.image">
                </div>
                <div class="col-8">
                    <p class="popover-header">{{news_data.header}}</p>
                    <p class="popover-header">{{news_data.body}}</p>
                    <p>{{news_data.post_date| formatDate }}</p>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import {APIService} from '../lenta-vue/APIService';
    const apiService = new APIService();

    export default {
        name: 'NewsPost',
        data() {
            return {
                news_data: {},
            };
        },
        methods: {
            getNewsPost(url){
                this.loading = true;
                apiService.getNewsPost(url).then((page) => {
                    this.news_data = page.data;
                    this.loading = false;
                });
            },
        },
        mounted() {
            this.getNewsPost(this.$route.params.url);
        },
    }
</script>
