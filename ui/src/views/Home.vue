<template>
  <div class="home">
    <main-header></main-header>
    <div class="components flex-column-start">
      <div class="section flex-column-start">
        <div class="header flex-row-center">
          <div class="icon flex-row-center">
            <img src="@/assets/svg/title-icon.svg">
          </div>
          <div class="header-text">{{ title }}</div>
        </div>
        <div class="legend">
          <div class="legend-icons">
            <div class="legend-item">
              <div class="legend-item-img">
                <div class="legend-item-text">Т</div>
                <img src="@/assets/svg/legend-t.svg">
              </div>
              <div class="legend-item-text">Температура</div>
            </div>
            <div class="legend-item">
              <div class="legend-item-img">
                <div class="legend-item-text">V</div>
                <img src="@/assets/svg/legend-v.svg">
              </div>
              <div class="legend-item-text">Вибрация</div>
            </div>
            <div class="legend-item">
              <div class="legend-item-img">
                <div class="legend-item-text">L</div>
                <img src="@/assets/svg/legend-o.svg">
              </div>
              <div class="legend-item-text">Уровень масла</div>
            </div>
            <div class="legend-item">
              <img src="@/assets/svg/legend-d.svg">
              <div class="legend-item-text">Предупреждение</div>
            </div>
            <div class="legend-item">
              <img src="@/assets/svg/legend-a.svg">
              <div class="legend-item-text">Опасность</div>
            </div>
          </div>
        </div>
        <div class="container content flex-column-start">
          <div class="row">
            <div v-for="machine in machines" class="machine-section">
              <div class="machine-title">Агломашина № {{ machine.id }}</div>
              <div class="machine-section-content">

                <div v-for="exhauster in machine.exhausters" class="card">
                  <div class="card-header">
                    <div class="card-title">
                      <img v-if="exhauster.status === 'normal'" src="@/assets/svg/green_circle.svg">
                      <img v-else src="@/assets/svg/red_circle.svg">
                      <div class="card-title-text">Эксгаустер {{ exhauster.name }}</div>
                    </div>
                    <div class="card-title-button">
                      <a :href="exhauster.id">
                        <img src="@/assets/svg/exhauster_btn.svg">
                      </a>
                    </div>
                  </div>
                  <div class="card-content">
                    <div class="card-content-header">
                      <div class="row card-content-header-title">
                        <div class="card-content-header-title-text">
                          Ротор № 35к
                          <div class="card-content-header-title-date">12.02.2022</div>
                          <div class="card-content-header-title-link">
                            <div class="card-content--link">Изменить</div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <svg width="260" height="2" viewBox="0 0 260 2" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <line y1="1.0249" x2="260" y2="1.0249" stroke="#EFEFEF"/>
                    </svg>
                    <div class="card-info">
                      <div class="card-info-group">
                        <div class="card-info-group-title">Последняя замена ротера</div>
                        <div class="card-info-content">
                          <div class="card-info-content-text">
                            <div class="card-info-content-text-main fw-bold">6 сут</div>
                            <div class="card-info-content-text-forecast flex-row-start">
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="card-scheme">
                      <div class="card-scheme-img">
                        <img src="@/assets/svg/rotor.svg">
                      </div>
                    </div>
                    <div v-if="exhauster.danger_signals.length > 0" class="card-items">
                      <div class="card-items-btn">
                        <img
                            v-if="!exhauster.btn_danger"
                            src="@/assets/svg/btn/open.svg"
                            @click="click_button(machine.id, exhauster.name, true)"
                        >
                        <img
                            v-else src="@/assets/svg/btn/close.svg"
                            @click="click_button(machine.id, exhauster.name, true)"
                        >
                      </div>
                      <div class="card-items-title">
                        <div class="card-items-title-text">Предупреждение</div>
                      </div>
                    </div>
                    <div v-if="exhauster.btn_danger && exhauster.danger_signals.length > 0" class="card-table">
                      <div v-for="danger_signal in exhauster.danger_signals" class="card-table-item">
                        <div class="card-table-coll-name">
                          <div class="card-table-coll-name-text">{{ danger_signal.name }}</div>
                        </div>
                        <div class="card-table-coll-value">
                          <div class="card-table-coll-value-frame">
                            <div v-if="danger_signal.temp">
                              <div :class="get_signal_class(danger_signal.temp.status)">
                                <div class="card-table-coll-value-frame-title">T</div>
                                <img src="@/assets/svg/signals/temp_normal.svg">
                              </div>
                            </div>
                            <div v-if="danger_signal.vibration">
                              <div :class="get_signal_class(danger_signal.vibration.status)">
                                <div class="card-table-coll-value-frame-title">V</div>
                                <img src="@/assets/svg/signals/temp_normal.svg">
                              </div>
                            </div>
                            <div v-if="danger_signal.oil">
                              <div :class="get_signal_class(danger_signal.oil.status)">
                                <div class="card-table-coll-value-frame-title">V</div>
                                <img src="@/assets/svg/signals/temp_normal.svg">
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="card-items">
                      <div class="card-items-btn">
                        <img
                            v-if="!exhauster.btn"
                            src="@/assets/svg/btn/open.svg"
                            @click="click_button(machine.id, exhauster.name, false)"
                        >
                        <img
                            v-else src="@/assets/svg/btn/close.svg"
                            @click="click_button(machine.id, exhauster.name, false)"
                        >
                      </div>
                      <div class="card-items-title">
                        <div class="card-items-title-text">Все подшипники</div>
                      </div>
                    </div>
                    <div v-if="exhauster.btn" class="card-table">
                      <div v-for="signal in exhauster.signals" class="card-table-item">
                        <div class="card-table-coll-name">
                          <div class="card-table-coll-name-text">{{ signal.name }}</div>
                        </div>
                        <div class="card-table-coll-value">
                          <div class="card-table-coll-value-frame">
                            <div v-if="signal.temp" class="card-table-coll-value-frame-normal">
                              <div class="card-table-coll-value-frame-title">T</div>
                              <img src="@/assets/svg/signals/temp_normal.svg">
                            </div>
                            <div v-if="signal.vibration" class="card-table-coll-value-frame-normal">
                              <div class="card-table-coll-value-frame-title">V</div>
                              <img src="@/assets/svg/signals/temp_normal.svg">
                            </div>
                            <div v-if="signal.oil" class="card-table-coll-value-frame-normal">
                              <div class="card-table-coll-value-frame-title">V</div>
                              <img src="@/assets/svg/signals/temp_normal.svg">
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import mainHeader from "../components/header";

export default {
  name: 'Home',
  components: {mainHeader},

  mixins: [],

  data() {
    return {
      title: 'Главный экран',
      data: null,
      machines: []
    }
  },

  created() {
    this.data = this.loadExgausters();
  },

  methods: {
    async loadExgausters() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/exgausters/`)
          .then(
              response => (this.data = response.data));
      console.log(this.data)
      this.parse_data(this.data)
    },

    parse_data(data) {
      let machineNumber = 0;
      let machine
      for (let item of data) {
        if (item.number % 2 !== 0) {
          console.log(item.number)
          machineNumber += 1;
          machine = {id: machineNumber, exhausters: []};
        }
        let exhauster = {
          id: item.number,
          status: "normal",
          name: item.name,
          signals: [],
          danger_signals: [],
          btn: false,
          btn_danger: false,
        }
        for (let signal of item.bearings_big) {
          let new_signal = {
            id: signal.number,
            name: "№ " + signal.number + " п-к",
            temp: {
              value: signal.temperature,
              status: "normal"
            },
            vibration: {
              value: signal.vibration_axial,
              status: "normal"
            }
          }
          exhauster.signals.push(new_signal);
        }
        let new_signal = {
          name: "Уровень масла",
          oil: {
            value: item.oil_system,
            status: "normal"
          }
        }
        exhauster.signals.push(new_signal);

        for (let signal of item.bearings_small) {
          let new_signal = {
            id: signal.number,
            name: "№ " + signal.number + " п-к",
            temp: {
              value: signal.temperature,
            }
          }
          exhauster.signals.push(new_signal)
        }

        machine.exhausters.push(exhauster)
        if (item.number % 2 !== 0) {
          this.machines.push(machine);
        }
      }
    },

    click_button(machine_id, exhauster_name, danger) {
      for (let machine of this.machines) {
        if (machine.id === machine_id) {
          for (let exhauster of machine.exhausters) {
            if (exhauster.name === exhauster_name) {
              if (danger === true) {
                exhauster.btn_danger = !exhauster.btn_danger;
              } else {
                exhauster.btn = !exhauster.btn;
              }
            }
          }
        }
      }
    },

    get_signal_class(status) {
      return "card-table-coll-value-frame-" + status
    },
  },
}
</script>


<style scoped>
.machine-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 10px;

  width: 650px;

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.machine-section-content {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 10px 0;
  gap: 10px;

  border-radius: 0px 4px 4px 4px;

  flex: none;
  order: 1;
  flex-grow: 0;
}

.machine-title {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 10px 20px;
  gap: 10px;

  background: #F4F4F4;
  border-radius: 4px 4px 0px 0px;

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}
</style>