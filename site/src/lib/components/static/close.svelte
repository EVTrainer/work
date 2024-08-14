<script lang="ts">
</script>

<a href="#" class="close"></a>

<style>
    .close {
        position: absolute;
        right: 5px;
        top: 10px;
        width: 32px;
        height: 32px;
        opacity: 0.6;
    }

    .close:hover {
        opacity: 1;
    }

    .close:before, .close:after {
        position: absolute;
        left: 15px;
        content: ' ';
        height: 15px;
        width: 1.5px;
        border-radius: 0.75px;
        background-color: var(--grack_gentle);
    }

    .close:before {
        transform: rotate(45deg);
    }

    .close:after {
        transform: rotate(-45deg);
    }
</style>