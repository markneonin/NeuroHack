import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";
import Dashboard from "@/pages/Dashboard.vue";
import TableList from "@/pages/TableList.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "",
    children: [
      {
        path: "",
        name: "Table List",
        component: TableList,
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard,
      },
    ],
  },
];

export default routes;
