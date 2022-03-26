import Vue from "vue";
import VueRouter from "vue-router";
import DeckLIstView from "@/views/DeckLIstView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: DeckLIstView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
