<template>
  <svg
    :class="isPrimary ? 'is-primary' : 'no-primary'"
    viewBox="0 0 20 20"
    width="20" height="20"
    xmlns="http://www.w3.org/2000/svg">
    <circle v-if="shape === 'circle'"
      cx="10" cy="10"
      :r="attr.size * 10 - attr.strokeWidth / 2"
      :stroke="attr.strokeColor"
      :stroke-width="attr.strokeWidth"
      :stroke-opacity="attr.strokeOpacity"
      :fill="attr.fillColor"
      :fill-opacity="attr.fillOpacity"
    />
    <rect v-else-if="shape === 'square'"
      :x="'0'"
      :y="'0'"
      :width="attr.size * 20 - attr.strokeWidth"
      :height="attr.size * 20 - attr.strokeWidth"
      :stroke-width="attr.strokeWidth"
      :stroke="attr.strokeColor"
      :stroke-opacity="attr.strokeOpacity"
      :fill="attr.fillColor"
      :fill-opacity="attr.fillOpacity"
      :transform="'translate('+
        ( (20-(attr.size * 20 - attr.strokeWidth)) / 2) +
        ' '+
        ( (20-(attr.size * 20 - attr.strokeWidth)) / 2) +
        ')'"
    />
    <line v-else-if="shape === 'line'"
      x1="0" x2="20"
      y1="10"
      y2="10"
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
