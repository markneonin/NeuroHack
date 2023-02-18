<template>
  <div class="home">
    <div class="main-header flex-row-center">
      <div class="logo-group">
        <img src="@/assets/svg/logo.svg">
      </div>
      <div class="breadcrumbs">Прогнозная аналитика эксгаустеров</div>
    </div>
    <div class="container components flex-column-start">
      <div class="section flex-column-start">
        <div class="header flex-row-center">
          <div class="icon flex-row-center">
            <img src="@/assets/svg/title-icon.svg">
          </div>
          {{ title }}
        </div>
        <div class="legend">
          <div class="legend-icons">
            <div class="legend-item">
              <div class="legend-item-img">
                Т
                <img src="@/assets/svg/legend-t.svg">
              </div>
              Температура
            </div>
            <div class="legend-item">
              <div class="legend-item-img">
                V
                <img src="@/assets/svg/legend-v.svg">
              </div>
              Вибрация
            </div>
            <div class="legend-item">
              <div class="legend-item-img">
                L
                <img src="@/assets/svg/legend-o.svg">
              </div>
              Уровень масла
            </div>
            <div class="legend-item">
              <img src="@/assets/svg/legend-d.svg">
              Предупреждение
            </div>
            <div class="legend-item">
              <img src="@/assets/svg/legend-a.svg">
              Опасность
            </div>
          </div>
        </div>

        <div class="container content flex-column-start">
          <div class="row">
            <div v-for="machine in machines" class="machine-section">
              <div class="title">Агломашина № {{ machine.id }}</div>
              <div class="machine-section-content">

                <div v-for="exhauster in machine.exhausters" class="card">
                  <div class="card-header">
                    <div class="card-title">
                      <img src="@/assets/svg/red_circle.svg">
                      <div class="card-title-text">Эксгаустер {{ exhauster.name }}</div>
                    </div>
                    <div class="card-title-button">
                      <img src="@/assets/svg/exhauster_btn.svg">
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
                              <div v-if="danger_signal.vol">
                                <div :class="get_signal_class(danger_signal.vol.status)">
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
                            <div v-if="signal.vol" class="card-table-coll-value-frame-normal">
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

export default {
  name: 'Home',
  components: {},

  mixins: [],

  data() {
    return {
      title: 'Главный экран',
      machines: [
        {
          id: 1,
          exhausters: [
            {
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
            {
              name: "У-172",
              signals: [
                {
                  id: 3,
                  name: "№1  п-к",
                  vol: {
                    value: 220,
                    status: "normal",
                  },
                  oil: null
                }
              ],
              danger_signals: [
                {
                  id: 10,
                  name: "Уровень масла",
                  oil: {
                    value: 50,
                    status: "alarm"
                  },
                }
              ],
              btn: false,
              btn_danger: false,
            },
          ],
        },
        {
          id: 2,
          exhausters: [
            {
              name: "У-173",
              signals: [
                {
                  id: 4,
                  name: "№1  п-к",
                  temp: {
                    value: 56,
                    status: "warning",
                  },
                  vol: {
                    value: 220,
                    status: "normal",
                  },
                  oil: null
                },
              ],
              danger_signals: [],
              btn: false,
              btn_danger: false,
            },
            {
              name: "У-174",
              signals: [
                {
                  id: 5,
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
                  id: 6,
                  name: "№2  п-к",
                  vol: {
                    value: 220,
                    status: "normal",
                  },
                  oil: null
                },
              ],
              danger_signals: [
                {
                  id: 4,
                  name: "№3  п-к",
                  temp: {
                    value: 56,
                    status: "warning",
                  },
                  vol: {
                    value: 220,
                    status: "normal",
                  },
                  oil: null
                },
                {
                  id: 6,
                  name: "№2  п-к",
                  vol: {
                    value: 220,
                    status: "alarm",
                  },
                  oil: null
                },
              ],
              btn: false,
              btn_danger: false,
            },
          ],
        },
      ]
    }
  },

  created() {
    console.log(this.$store.getters.getServerUrl)
  },

  methods: {
    async loadExgausters() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/exhausters/`)
          .then(response => (this.exhausters = response.data));
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
    }

  },
}
</script>


<style scoped>
</style>