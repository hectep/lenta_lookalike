<template>
  <div id="app">
    <div>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="btn btn-primary" href="/">News</a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
    <div class="jumbotron">
      <router-view/>
    </div>
  </div>
</template>

<script>
  export default {
  }
</script>

<style>
  @import './assets/bootstrap/css/bootstrap.min.css';

  body {
    min-height: 75rem;
    padding-top: 4.5rem;
  }
  .nav-item{
    padding:1px;
    margin-left: 5px;
  }
</style>

