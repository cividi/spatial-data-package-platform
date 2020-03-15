<template>
  <svg
    :class="isPrimary ? 'is-primary' : 'no-primary'"
    viewBox="0 0 20 20"
    width="20" height="20"
    xmlns="http://www.w3.org/2000/svg">
    <circle v-if="shape === 'circle'"
      cx="10" cy="10"
      :r="9 * attr.size"
      :stroke="attr.strokeColor"
      :stroke-width="attr.strokeWidth"
      :stroke-opacity="attr.strokeOpacity"
      :fill="attr.fillColor"
      :fill-opacity="attr.fillOpacity"
    />
    <rect v-else-if="shape === 'square'"
      :x="'calc(50% - ' + attr.size * 10 + ')'"
      :y="'calc(50% - ' + attr.size * 10 + ')'"
      :width="attr.size * 20"
      :height="attr.size * 20"
      :stroke-width="attr.strokeWidth"
      :stroke="attr.strokeColor"
      :stroke-opacity="attr.strokeOpacity"
      :fill="attr.fillColor"
      :fill-opacity="attr.fillOpacity"
    />
    <line v-else-if="shape === 'line'"
      x1="0" x2="100%"
      y1="50%"
      y2="50%"
      :stroke="attr.strokeColor"
      :stroke-width="attr.strokeWidth"
      :opacity="attr.strokeOpacity"
    />
  </svg>
</template>

<style>
</style>


<script>
export default {
  name: 'LegendIcon',
  data() {
    return {};
  },

  props: {
    shape: String,
    isPrimary: Boolean,
    attr: Object
  }
};
</script>
