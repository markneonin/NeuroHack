<template>
  <div class="wrapper">
    <side-bar>
      <sidebar-link to="/">
        <i class="tim-icons icon-align-center"></i>
        <template>
          <p>Главная</p>
        </template>
      </sidebar-link>
      <sidebar-link to="/dashboard">
        <i class="tim-icons icon-chart-pie-36"></i>
        <template>
          <p>Тренды</p>
        </template>
      </sidebar-link>
    </side-bar>
    <sidebar-share></sidebar-share>
    <div class="main-panel">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar"></dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>

<style lang="scss"></style>

<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./DashboardContent.vue";
import MobileMenu from "./MobileMenu.vue";
import SideBar from "@/components/SidebarPlugin/SideBar.vue";
import SidebarLink from "@/components/SidebarPlugin/SidebarLink.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu,
    SideBar,
    SidebarLink,
  },

  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
