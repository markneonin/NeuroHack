<template>
  <div class="exhauster">
    <main-header :title="getTitle()"></main-header>
    <div class="filters">
      <div class="filters-date"></div>
      <div class="filters-switch">
        <div class="filters-switch-buttons">
          <button class="active-switch-button">Моносхема</button>
          <button class="switch-button">График</button>
        </div>
      </div>
    </div>
    <div class="components flex-column-start">
      <div class="section flex-column-start">
        <div class="header flex-row-center">
          <div class="icon flex-row-center">
            <img src="@/assets/svg/title-icon.svg">
          </div>
          <div class="header-text">Эксгаустер {{ exhauster.name }}</div>
        </div>
        <schema v-if="mode === 'schema'"></schema>
        <threads v-if="mode === 'threads'"></threads>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import mainHeader from "../components/header";
import Schema from "../components/schema"
import threads from "../components/threads"

export default {
  name: "Exhauster",
  components: {mainHeader, Schema, threads},
  props: ['id', 'data'],

  data() {
    return {
      mode: 'schema',
      exhauster: {
        name: "У-171",
        signals: [
          {
            id: 1,
            name: "№1  п-к",
            temp: {
              value: 56,
              status: "normal",
            },
            vol: {
              value: 220,
              status: "normal",
            },
            oil: null
          },
          {
            id: 2,
            name: "№2  п-к",
            temp: {
              value: 56,
              status: "normal",
            },
            oil: null
          },
          {
            id: 10,
            name: "Уровень масла",
            oil: {
              value: 50,
              status: "normal"
            },
          }
        ],
        danger_signals: [],
        btn: false,
        btn_danger: false,
      },
    }
  },

  methods:{
    getTitle() {
      return " / Состояние эксгаустера " + this.exhauster.name
    }
  },
}
</script>

<style scoped>
.switch-button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 5px 12px;
  border: none;

  width: 110px;

  font-style: normal;
  font-weight: 500;
  background: #FFFFFF;
  border-radius: 4px;
  color: #F9A823;

  flex: none;
  order: 1;
  flex-grow: 0;
}

.active-switch-button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 5px 12px;
  border: none;

  width: 110px;

  font-style: normal;
  font-weight: 500;
  color: #000000;
  background: #FAB82E;
  border-radius: 4px;

  flex: none;
  order: 0;
  flex-grow: 0;
}
</style>