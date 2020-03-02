<template>
  <div>
    <p>{{ title }}</p>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'SnapshotMeta',
  data() {
    return {};
  },
  props: {
    title: String,
    description: String
  }
};
</script>
