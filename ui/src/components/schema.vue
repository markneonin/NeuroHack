<template>
  <div class="schema">
    <div class="schema-area container">
      <div class="rectangle-line">
        <img src="@/assets/svg/machine/rectangle-line.svg">
      </div>
      <div class="rectangle-line-2">
        <img src="@/assets/svg/machine/rectangle-line.svg">
      </div>
      <div class="cooler-area">
        <div class="cooler-title">Охладитель</div>
        <div class="cooler_image">
          <img src="@/assets/svg/machine/cooler.svg">
        </div>
        <div class="cooler-in">
          <img src="@/assets/svg/machine/cooler-in.svg">
        </div>
        <div class="cooler-out">
          <img src="@/assets/svg/machine/cooler-out.svg">
        </div>
        <div class="cooler_value_oot">
          <div class="cooler_value_text">{{ Math.ceil((data.cooler.oil_temperature_after)*100)/100 }} °С</div>
        </div>
        <div class="cooler_value_in">
          <div class="cooler_value_text">{{ Math.ceil((data.cooler.oil_temperature_before)*100)/100 }} °С</div>
        </div>
        <div class="cooler_value_left">
          <div class="cooler_value_text">{{ Math.ceil((data.cooler.oil_temperature_after)*100)/100 }} °С</div>
        </div>
        <div class="cooler_value_bottom">
          <div class="cooler_value_text">{{ Math.ceil((data.cooler.water_temperature_before)*100)/100 }} °С</div>
        </div>
      </div>
      <div class="oil_area">
        <div class="oil_frame">
          <div class="oil_frame_values">
            <div class="oil_frame_values_item">
              <div class="oil_frame_values_item_text">0</div>
            </div>
            <div class="oil_frame_values_item">
              <div class="oil_frame_sep"></div>
              <div class="oil_frame_values_item_text">20</div>
            </div>
            <div class="oil_frame_values_item">
              <div class="oil_frame_sep"></div>
              <div class="oil_frame_values_item_text">40</div>
            </div>
            <div class="oil_frame_values_item">
              <div class="oil_frame_sep"></div>
              <div class="oil_frame_values_item_text">60</div>
            </div>
            <div class="oil_frame_values_item">
              <div class="oil_frame_sep"></div>
              <div class="oil_frame_values_item_text">80</div>
            </div>
            <div class="oil_frame_values_item">
              <div class="oil_frame_sep"></div>
              <div class="oil_frame_values_item_text">100</div>
            </div>
          </div>
          <div class="oil_frame_info">
            <div class="oil_chart">
              <div class="oil_chart_info">
                <div class="oil_chart_alarm">
                  <div class="oil_chart_value">34,3</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="oil_header">
          <div class="oil_header_text">Маслобак</div>
        </div>
        <div class="oil_to_cooler_line">
          <img src="@/assets/svg/machine/oil_to_cooler_line.svg">
        </div>
      </div>
      <div class="gaz-block">
        <div class="gaz-up-section">
          <div class="gaz_info">
            <div class="gaz_info_temp">
              <div class="gaz_info_temp_list">
                <div class="gaz_info_temp_list_chart">
                  <div class="gaz_info_temp_list_frame">
                    <div class="gaz_info_normal">
                      <div class="gaz_info_t">45</div>
                      <div class="gaz_info_desc">Температура газа,°C</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="gaz_table">
              <div class="gaz_table_item">
                <div class="gaz_table_text_block">
                  <div class="gaz_table_text">Разряжение</div>
                </div>
                <div class="gaz_table_value_block">
                  <div class="gaz_table_value">74,3</div>
                </div>
              </div>
              <div class="gaz_table_item">
                <div class="gaz_table_text_block">
                  <div class="gaz_table_text">Уровень пыли</div>
                </div>
                <div class="gaz_table_value_block">
                  <div class="gaz_table_value">15</div>
                </div>
              </div>
            </div>
          </div>
          <img src="@/assets/svg/machine/gaz-top.svg">
        </div>
        <div class="gaz-down-section">
          <img src="@/assets/svg/machine/gaz-down.svg">
          <div class="damper50">
            <img src="@/assets/svg/machine/damper50.svg">
          </div>
        </div>
        <img src="@/assets/svg/machine/gaz.svg">
      </div>
      <div class="rectangle-mf">
        <img src="@/assets/svg/machine/rectangle-mf.svg">
      </div>
      <div class="group-pk-1">
        <div class="line_bottom">
          <img src="@/assets/svg/machine/line_bottom.svg">
        </div>
        <img src="@/assets/svg/machine/pk.svg">
        <div class="pk-top-warning">
          <div class="pk-text">1</div>
        </div>
        <div class="reductor-frame-right-bottom">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">1 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-normal">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsBig('1'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">В,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalInBearingsBig('1'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">Г,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalHorizontalInBearingsBig('1'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">O,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalAxialInBearingsBig('1'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="group-pk-2">
        <div class="line_bottom">
          <img src="@/assets/svg/machine/line_bottom.svg">
        </div>
        <img src="@/assets/svg/machine/pk.svg">
        <div class="pk-top-normal">
          <div class="pk-text">2</div>
        </div>
        <div class="reductor-frame-right-bottom">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">2 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-normal">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsBig('2'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">В,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalInBearingsBig('2'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">Г,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalHorizontalInBearingsBig('2'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">O,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalAxialInBearingsBig('2'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="reductor">
        <div class="reductor-to-oil-line">
          <img src="@/assets/svg/machine/reductor-to-oil.svg">
        </div>
        <div class="rotor-to-main-line">
          <img src="@/assets/svg/machine/rotor-to-main-line.svg">
        </div>
        <div class="reductor-frame-left-top">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">4 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-normal">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsSmall('4'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="reductor-line-left-top">
          <img src="@/assets/svg/machine/reductor-left-top.svg">
        </div>
        <div class="reductor-frame-right-top">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">5 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-warning">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsSmall('5'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="reductor-line-right-top">
          <img src="@/assets/svg/machine/reductor-right-top.svg">
        </div>
        <div class="reductor-frame-left-bottom">
          <div class="frame-params">
            <div class="frame-params">
              <div class="frame-params">
                <div class="frame_select">
                  <div class="frame_title">
                    <div class="frame_title_text">6 ПС</div>
                  </div>
                </div>
                <div class="frame-dropdown">
                  <div class="frame-table">
                    <div class="frame-table-normal">
                      <div class="frame-table-key">T,°С</div>
                      <div class="frame-table-value">
                        {{ Math.ceil((getTemperatureInBearingsSmall('6'))*100)/100 }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="reductor-line-left-bottom">
          <img src="@/assets/svg/machine/reductor-left-bottom.svg">
        </div>
        <div class="reductor-frame-right-bottom">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">3 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-alarm">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsSmall('3'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="reductor-line-right-bottom">
          <img src="@/assets/svg/machine/reductor-right-bottom.svg">
        </div>
        <div class="reductor-rectangle">
          <div class="reductor-title">Редуктор</div>
          <div class="pk-3-warning">
            <div class="pk-text">3</div>
          </div>
          <div class="pk-4-normal">
            <div class="pk-text">4</div>
          </div>
          <div class="pk-5-normal">
            <div class="pk-text">5</div>
          </div>
          <div class="pk-6-normal">
            <div class="pk-text">6</div>
          </div>
        </div>
      </div>
      <div class="main-privod">
        <div class="main-privod-down-line">
          <svg width="13" height="400" viewBox="0 0 13 281" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
                d="M12.8259 273.903C12.8259 277.313 10.0618 280.077 6.65208 280.077H0.825928V269.974H12.8259V273.903V273.903Z"
                fill="#677272"/>
            <path d="M9.82593 273.342C9.82593 275.202 8.31822 276.709 6.45838 276.709H0.825928V273.342H9.82593V273.342Z"
                  fill="white"/>
            <rect width="9" height="157.665" transform="matrix(1 0 0 -1 3.82593 270.742)" fill="#677272"/>
            <rect width="3" height="159.078" transform="matrix(1 0 0 -1 6.82593 275.155)" fill="white"/>
          </svg>
        </div>
        <div class="main-to-cooler-line">
          <img src="@/assets/svg/machine/main-to-coler-line.svg">
        </div>
        <img src="@/assets/svg/machine/main-block.svg">
      </div>
      <div class="group-pk-7">
        <img src="@/assets/svg/machine/pk.svg">
        <div class="pk-down-alarm">
          <div class="pk-text">7</div>
        </div>
        <div class="line_bottom-7">
          <img src="@/assets/svg/machine/line-bottom-7.svg">
        </div>
        <div class="line_right-7">
          <img src="@/assets/svg/machine/line-right-7.svg">
        </div>
        <div class="line_right-bottom-7">
          <img src="@/assets/svg/machine/line-right-bottom-7.svg">
        </div>
        <div class="line_right-bottom-right-7">
          <img src="@/assets/svg/machine/line-right-bottom-right-7.svg">
        </div>
        <div class="frame7">
          <div class="frame-params">
            <div class="frame-params">
              <div class="frame_select">
                <div class="frame_title">
                  <div class="frame_title_text">7 ПС</div>
                </div>
              </div>
              <div class="frame-dropdown">
                <div class="frame-table">
                  <div class="frame-table-normal">
                    <div class="frame-table-key">T,°С</div>
                    <div class="frame-table-value">
                      {{ Math.ceil((getTemperatureInBearingsBig('7'))*100)/100 }}
                    </div>
                  </div>
                  <div class="frame-table-normal">
                    <div class="frame-table-key">В,мм/с</div>
                    <div class="frame-table-value">
                      {{ Math.ceil((getVibrationVerticalInBearingsBig('7'))*100)/100 }}
                    </div>
                  </div>
                  <div class="frame-table-normal">
                    <div class="frame-table-key">Г,мм/с</div>
                    <div class="frame-table-value">
                      {{ Math.ceil((getVibrationVerticalHorizontalInBearingsBig('7'))*100)/100 }}
                    </div>
                  </div>
                  <div class="frame-table-normal">
                    <div class="frame-table-key">O,мм/с</div>
                    <div class="frame-table-value">
                      {{ Math.ceil((getVibrationVerticalAxialInBearingsBig('7'))*100)/100 }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="group-pk-89">
        <img src="@/assets/svg/machine/pk.svg">
        <div class="pk-top-normal">
          <div class="pk-text">9</div>
        </div>
        <div class="pk-down-warning">
          <div class="pk-text">8</div>
        </div>
        <div class="line_bottom-89">
          <img src="@/assets/svg/machine/line89.svg">
        </div>
        <div class="line_left-89">
          <img src="@/assets/svg/machine/line-left89.svg">
        </div>
        <div class="frame8">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">8 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-normal">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsBig('8'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">В,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalInBearingsBig('8'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">Г,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalHorizontalInBearingsBig('8'))*100)/100 }}
                  </div>
                </div>
                <div class="frame-table-normal">
                  <div class="frame-table-key">O,мм/с</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getVibrationVerticalAxialInBearingsBig('8'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="frame9">
          <div class="frame-params">
            <div class="frame_select">
              <div class="frame_title">
                <div class="frame_title_text">9 ПС</div>
              </div>
            </div>
            <div class="frame-dropdown">
              <div class="frame-table">
                <div class="frame-table-warning">
                  <div class="frame-table-key">T,°С</div>
                  <div class="frame-table-value">
                    {{ Math.ceil((getTemperatureInBearingsSmall('9'))*100)/100 }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="oil_pressure_section">
        <div class="oil_pressure_chart_desc">
          Давление масла, кг/см2
        </div>
        <div class="oil_frame_values">
          <div class="oil_frame_values_item">
            <div class="oil_frame_values_item_text">1</div>
          </div>
          <div class="oil_frame_values_item">
            <div class="oil_pressure_section_sep"></div>
            <div class="oil_frame_values_item_text">2</div>
          </div>
          <div class="oil_frame_values_item">
            <div class="oil_pressure_section_sep"></div>
            <div class="oil_frame_values_item_text">3</div>
          </div>
          <div class="oil_frame_values_item">
            <div class="oil_pressure_section_sep"></div>
            <div class="oil_frame_values_item_text">4</div>
          </div>
          <div class="oil_frame_values_item">
            <div class="oil_pressure_section_sep"></div>
            <div class="oil_frame_values_item_text">5</div>
          </div>
          <div class="oil_frame_values_item">
            <div class="oil_pressure_section_sep"></div>
            <div class="oil_frame_values_item_text">6</div>
          </div>
        </div>
        <div class="oil_frame_info">
          <div class="oil_chart">
            <div class="oil_chart_info">
              <div class="oil_pressure_chart_warning">
                <div class="oil_chart_value">2,5</div>
              </div>
            </div>
          </div>
        </div>
        <div class="oil_pressure_section_line">
          <svg width="76" height="10" viewBox="0 0 76 10" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="6.81421" y="9.0741" width="9" height="68.5115" transform="rotate(-90 6.81421 9.0741)"
                  fill="#677272"/>
            <rect x="0.769287" y="6.07324" width="3" height="74.5566" transform="rotate(-90 0.769287 6.07324)"
                  fill="white"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Schema",

  props: ['data'],

  methods: {
    getTemperatureInBearingsBig(id) {
      for (let bear of this.data.bearings_big) {
        if (bear.number == id ) {
          return bear.temperature
        }
      }
    },

    getTemperatureInBearingsSmall(id) {
      for (let bear of this.data.bearings_small) {
        if (bear.number == id ) {
          return bear.temperature
        }
      }
    },

    getVibrationVerticalInBearingsBig(id) {
      for (let bear of this.data.bearings_big) {
        if (bear.number == id ) {
          return bear.temperature
        }
      }
    },

    getVibrationVerticalHorizontalInBearingsBig(id) {
      for (let bear of this.data.bearings_big) {
        if (bear.number == id ) {
          return bear.vibration_horizontal
        }
      }
    },

    getVibrationVerticalAxialInBearingsBig(id) {
      for (let bear of this.data.bearings_big) {
        if (bear.number == id ) {
          return bear.vibration_axial
        }
      }
    },
  }
}
</script>

<style scoped>
</style>