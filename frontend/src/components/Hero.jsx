import hero from '../assets/images/hero-bg.png'

const Hero = () => {
  return (
  <div className=' md:h-screen flex flex-col-reverse md:flex-row md:justify-between items-center my-5  '>
      <div className='md:flex-1 '>
        <h1 className='text-4xl md:text-7xl font-semibold py-5'>manage your finances easily and more efficient</h1>
        <p className='text-xl md:text-2xl pb-5 text-gray-500'>your convinience and comfort in managing<br/> day to day finances</p>
        <button className=' border-2 px-5 py-2'>Lets get started</button>
    </div>
    <div className='md:flex-1 w-full'>
        <img src={hero} alt="" />
    </div>
  </div>
  )
}

export default Hero